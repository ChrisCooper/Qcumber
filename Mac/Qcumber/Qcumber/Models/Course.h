//
//  Course.h
//  Qcumber
//
//  Created by Chris Cooper on 11-10-19.
//  Copyright (c) 2011 Chris Cooper. All rights reserved.
//

#import <Foundation/Foundation.h>
#import <CoreData/CoreData.h>

@class Section, Subject;

@interface Course : NSManagedObject {

@private

}

@property (nonatomic, retain) NSString * desc;
@property (nonatomic, retain) NSString * key;
@property (nonatomic, retain) NSString * num;
@property (nonatomic, retain) NSString * title;
@property (nonatomic, retain) NSSet *sections;
@property (nonatomic, retain) Subject *subject;

@end

@interface Course (CoreDataGeneratedAccessors)

- (void)addSectionsObject:(Section *)value;
- (void)removeSectionsObject:(Section *)value;
- (void)addSections:(NSSet *)values;
- (void)removeSections:(NSSet *)values;

@end
