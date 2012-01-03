//
//  Course.h
//  Qcumber
//
//  Created by Chris Cooper on 12-01-01.
//  Copyright (c) 2012 __MyCompanyName__. All rights reserved.
//

#import <Foundation/Foundation.h>
#import <CoreData/CoreData.h>

@class Section, Subject;

@interface Course : NSManagedObject

@property (nonatomic, strong) NSString * descr;
@property (nonatomic, strong) NSNumber * number;
@property (nonatomic, strong) NSString * title;
@property (nonatomic, strong) NSSet *sections;
@property (nonatomic, strong) Subject *subject;
@end

@interface Course (CoreDataGeneratedAccessors)

- (void)addSectionsObject:(Section *)value;
- (void)removeSectionsObject:(Section *)value;
- (void)addSections:(NSSet *)values;
- (void)removeSections:(NSSet *)values;

@end
