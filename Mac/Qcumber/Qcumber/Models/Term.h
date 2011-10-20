//
//  Term.h
//  Qcumber
//
//  Created by Chris Cooper on 11-10-19.
//  Copyright (c) 2011 Chris Cooper. All rights reserved.
//

#import <Foundation/Foundation.h>
#import <CoreData/CoreData.h>

@class Section;

@interface Term : NSManagedObject {
@private
}
@property (nonatomic, retain) NSString * season;
@property (nonatomic, retain) NSString * year;
@property (nonatomic, retain) NSSet *sections;
@end

@interface Term (CoreDataGeneratedAccessors)

- (void)addSectionsObject:(Section *)value;
- (void)removeSectionsObject:(Section *)value;
- (void)addSections:(NSSet *)values;
- (void)removeSections:(NSSet *)values;
@end
